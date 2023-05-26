# simple-qr-generator

Generate high-quality QR codes from URLs using this Python script. This script utilizes the `qrcode` library to create QR codes in PNG format. It provides a simple command-line interface that prompts the user to enter the URL, output file name, and size of the QR code.

## Installation

1. Ensure you have Python 3 installed on your system.
2. Clone this repository or download the `qr_code_generator.py` file.
3. Install the required dependencies by running the following command: 
```
pip install qrcode
```

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where the `qr_code_generator.py` file is located.
3. Run the script using the following command:
```
python qr_code_generator.py
```
4. Follow the on-screen prompts to enter the URL, output file name, and size of the QR code.
5. The generated QR code will be saved as a PNG file in the same directory.

## Example

Let's say you want to generate a QR code for the URL `https://example.com` with a size of 200 pixels. You would run the script, enter the URL, provide an output file name (e.g., `example_qr_code`), and specify the size as 200. The script will generate a QR code and save it as `example_qr_code.png`.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [GNU General Public License (GPL) version 3](LICENSE).
