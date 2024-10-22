# WhistleC - Cooker Whistle Detection

WhistleC is a Java-based project that detects and counts cooker whistles in real-time using Fast Fourier Transform (FFT) for audio frequency analysis. This project is in its **initial phase** and may not be 100% efficient. Future updates will include improvements.

## Features
- Real-time whistle detection and counting.
- Frequency analysis using FFT.
- Detects whistles within 1000-3000 Hz.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/meYash05/WhistleC.git
   cd WhistleC

2. **Install Dependencies:**
   ```bash
      mvn clean install

3. **Run the Program:**
   ```bash
      mvn exec:java -Dexec.mainClass="com.yash.whistlecounter.WhistleC"

## Dependencies
This project relies on the following libraries and APIs:

   1. JTransforms (for Fast Fourier Transform): JTransforms GitHub
   2. Java Sound API (for capturing audio): Built into the Java platform.

These dependencies are managed automatically through Maven.

## Project Structure

WhistleC/
├── src/
│   └── main/
│       └── java/
│           └── com/
│               └── yash/
│                   └── whistlecounter/
│                       └── WhistleC.java
├── pom.xml
├── README.md
└── .gitignore

• src/main/java/com/yash/whistlecounter/WhistleC.java: The main Java file containing the logic for detecting cooker whistles.

• pom.xml: Maven configuration file that manages dependencies and project structure.

## License
This is an individual project, and all rights are reserved by the author. No part of this project may be reproduced, distributed, or transmitted in any form without prior permission.

## Contributing
   Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/your-feature).
3. Make your changes and commit them (git commit -am 'Add some feature').
4. Push to the branch (git push origin feature/your-feature).
5. Open a Pull Request.

## Note
This project is currently in its initial phase. While the basic functionality of detecting cooker whistles is working, it might not be 100% accurate or efficient in all cases. Future updates will include optimizations to improve the detection accuracy and reduce false positives.


