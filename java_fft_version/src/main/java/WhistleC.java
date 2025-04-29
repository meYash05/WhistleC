import javax.sound.sampled.*;
import javax.swing.*;
import java.awt.*;
import java.util.Arrays;
import org.jtransforms.fft.DoubleFFT_1D;

public class WhistleC extends JPanel {

    private static final double WHISTLE_MIN_FREQUENCY = 1000;
    private static final double WHISTLE_MAX_FREQUENCY = 3000;
    private static final double DETECTION_THRESHOLD = 150;

    private int whistleCount = 0;
    private boolean isWhistleDetected = false;
    private double[] latestMagnitudes;
    private final float sampleRate = 16000;

    public static void main(String[] args) {
        WhistleC visualizer = new WhistleC();
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Whistle Frequency Visualizer");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(1000, 400);
            frame.add(visualizer);
            frame.setVisible(true);
        });
        visualizer.captureAudio();
    }

    public void captureAudio() {
        try {
            AudioFormat format = new AudioFormat(sampleRate, 16, 1, true, true);
            DataLine.Info info = new DataLine.Info(TargetDataLine.class, format);

            if (!AudioSystem.isLineSupported(info)) {
                System.out.println("[ERROR] Microphone not supported.");
                return;
            }

            TargetDataLine microphone = (TargetDataLine) AudioSystem.getLine(info);
            microphone.open(format);
            microphone.start();
            System.out.println("[INFO] Microphone started. Listening for whistles...");

            int bufferSize = 4096;
            byte[] buffer = new byte[bufferSize];
            double[] audioData = new double[bufferSize / 2];

            DoubleFFT_1D fft = new DoubleFFT_1D(audioData.length);

            while (true) {
                int bytesRead = microphone.read(buffer, 0, buffer.length);
                for (int i = 0, j = 0; i < bytesRead - 1; i += 2, j++) {
                    int sample = (buffer[i] << 8) | (buffer[i + 1] & 0xFF);
                    audioData[j] = sample / 32768.0;
                }

                double[] fftData = Arrays.copyOf(audioData, audioData.length);
                fft.realForward(fftData);

                double[] magnitudes = new double[fftData.length / 2];
                for (int i = 0; i < magnitudes.length; i++) {
                    double re = fftData[2 * i];
                    double im = fftData[2 * i + 1];
                    magnitudes[i] = Math.sqrt(re * re + im * im);
                }

                latestMagnitudes = magnitudes;
                repaint();

                int detectedIndex = detectWhistleFrequencyIndex(magnitudes);
                if (detectedIndex != -1 && !isWhistleDetected) {
                    whistleCount++;
                    isWhistleDetected = true;
                    double freq = (double) detectedIndex * sampleRate / (audioData.length * 2);
                    System.out.println("[DETECTED] Whistle #" + whistleCount + " at frequency: " + freq + " Hz");
                } else if (detectedIndex == -1) {
                    isWhistleDetected = false;
                }
            }
        } catch (Exception e) {
            System.out.println("[ERROR] " + e.getMessage());
        }
    }

    private int detectWhistleFrequencyIndex(double[] magnitudes) {
        double maxMagnitude = 0;
        int index = -1;
        int minIndex = (int) (WHISTLE_MIN_FREQUENCY * magnitudes.length * 2 / sampleRate);
        int maxIndex = (int) (WHISTLE_MAX_FREQUENCY * magnitudes.length * 2 / sampleRate);

        for (int i = minIndex; i <= maxIndex; i++) {
            if (magnitudes[i] > maxMagnitude && magnitudes[i] > DETECTION_THRESHOLD) {
                maxMagnitude = magnitudes[i];
                index = i;
            }
        }
        return index;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        if (latestMagnitudes == null) return;

        Graphics2D g2d = (Graphics2D) g;
        g2d.setColor(Color.BLACK);
        g2d.fillRect(0, 0, getWidth(), getHeight());

        int width = getWidth();
        int height = getHeight();
        int len = latestMagnitudes.length;

        g2d.setColor(Color.GREEN);
        for (int i = 0; i < len - 1; i++) {
            int x1 = i * width / len;
            int x2 = (i + 1) * width / len;
            int y1 = height - (int) (latestMagnitudes[i] * 5);
            int y2 = height - (int) (latestMagnitudes[i + 1] * 5);
            g2d.drawLine(x1, y1, x2, y2);
        }

        // Draw threshold line in red
        g2d.setColor(Color.RED);
        int thresholdY = height - (int) (DETECTION_THRESHOLD * 5);
        g2d.drawLine(0, thresholdY, width, thresholdY);
    }
}
