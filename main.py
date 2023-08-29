import argparse
from server import serve
from printer import PrinterDriver  # Assuming printer.py has a Printer class

def main():
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description='Send images or text to the printer.')
    parser.add_argument('--image', type=str, help='Path to the image file to be printed.')
    parser.add_argument('--text', type=str, help='Text string to be printed.')
    args = parser.parse_args()

    # If image or text arguments are provided, print them. Otherwise, start the server.
    if args.image or args.text:
        printer_instance = PrinterDriver()  # Initialize the printer instance
        if args.image:
            printer_instance.print_image(args.image)
        if args.text:
            printer_instance.print_text(args.text)
    else:
        serve()  # Start the server if no arguments are provided

if __name__ == "__main__":
    main()
