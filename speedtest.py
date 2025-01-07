# THE code below runs test on your device and is able to run your interned speeds in Mbps
!pip install speedtest-cli
from IPython import get_ipython
from IPython.display import display, HTML # Import the HTML class
import speedtest

test = speedtest.Speedtest()
download = test.download() / 8000000  # Convert to Mbps
upload = test.upload() / 8000000  # Convert to Mbps

print("Code9t codes\nThis code checks the interned speed of your ISP \n click Run button below to check your speed\n")
button_html = '''
<button style="background-color:green; border:none; border-radius:15px;">Run</button>
'''

display(HTML(button_html)) # Now HTML is defined and can be used
print("\nSpeedtest Results are as follows:")
print(f"DOWNLOAD SPEED = {download:.2f} Mbps")  # Format to 2 dp
print(f"UPLOAD SPEED = {upload:.2f} Mbps")  # Format to 2 dp