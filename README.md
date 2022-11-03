# subnet_calculator
For doing calculations related to subnet design (written as tool for CS4121 subnet pre-lab)


subnet_calculator.py takes input from the console for first address as integer (i.e., 10.10.24.X, where X is the inputted value) and at least one integer as the requested host amount. It then determines if the user wants additional subnet host requests and will continue until user says they are finished.

It then displays the LANs in descending order of host amounts, giving the network, gateway, and broadcast address for that LAN. Current, string output is hardcoded with IP address values consistent with pre-lab requirements.

An example of use:
![image](https://user-images.githubusercontent.com/67984700/199848842-34e38b0c-4441-48c9-8fc4-bf2b4d455f70.png)
