import os
import time
import subprocess

# set directory path
directory = "/docx2pdf"

# initialize last conversion time as current time
last_conversion_time = time.time()

while True:
    # loop through each file in directory
    print(f"Checking directory for new files...")
    for filename in os.listdir(directory):
        # check if file is a docx file
        print(f"Checking {filename}...")
        if filename.endswith(".docx"):
            # create input and output file paths
            print(f"Found {filename}! Converting to PDF...")
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, f"{os.path.splitext(filename)[0]}.pdf")

            # check if PDF already exists
            print(f"Checking if {output_path} already exists...")
            if os.path.isfile(output_path):
                print(f"{output_path} already exists. Skipping conversion.")
            else:
                # check if file has been modified since last conversion
                print(f"Checking if {input_path} has been modified since last conversion...")
                if os.path.getmtime(input_path) > last_conversion_time:
                    # create PDF converter command
                    print(f"Converting {input_path} to {output_path}...")
                    cmd = ["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", directory, input_path]

                    # convert docx to pdf using libreoffice
                    subprocess.run(cmd)

                    print(f"{input_path} converted to {output_path}")

                    # update last conversion time to current time
                    last_conversion_time = time.time()

    # wait for 10 seconds before looping again
    time.sleep(10)
