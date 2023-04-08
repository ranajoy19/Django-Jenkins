Open an SSH client.

Locate your private key file. The key used to launch this instance is my-test-ec2.pem

Run this command, if necessary, to ensure your key is not publicly viewable.
 chmod 400 my-test-ec2.pem

Connect to your instance using its Public DNS:
 ec2-13-127-122-181.ap-south-1.compute.amazonaws.com

Example:
 
 ssh -i "my-test-ec2.pem" ubuntu@ec2-15-206-93-182.ap-south-1.compute.amazonaws.com