# HTB (HackTheBox) Solutions & Write-ups

This repository contains my solutions, write-ups, and tools for HackTheBox challenges and machines.

## Contents

### CTF Challenges

Solutions and write-ups for various types of CTF challenges:

**dec.py (dec means decryption, my favorite ctf categroy) is the solustion python code.**

#### AI/Machine Learning
- AISPACE
- FullOfStars 
- LikeAGlove
- LostInHyperspace
- SpinGlassBrain
- And more...

#### Blockchain
- Blockchain Confidentiality
- Distract and Destroy
- False Bidding
- Funds Secured
- Honor Among Thieves
- And more...

#### Crypto
Various cryptographic challenges including:
- RSA challenges
- AES implementations
- Hash challenges
- Custom encryption algorithms
- Protocol implementations

#### Hardware (HW)
Hardware and low-level challenges:
- BareMetal
- DebuggingInterface
- Factory
- Line
- MissionPinpossible
- And more...

#### OSINT
Open Source Intelligence challenges:
- BlockHunt3r
- EasyPhish
- IDExposed
- MissingInAction
- And more...

#### Web
Web application security challenges including:
- Authentication bypasses
- XSS exploits
- SQLi
- File upload vulnerabilities
- Server-side vulnerabilities

### Machines

Complete walkthrough files for various HTB machines. Each machine directory typically contains:
- Command history (cmd.txt)
- Custom exploit scripts
- Required binaries/tools
- Privilege escalation techniques

Some notable machines:
- Arctic (10.10.10.11)
- Bastard (10.10.10.9)
- Beep (10.10.10.7)
- Devel (10.10.10.5)
- Grandpa (10.10.10.14)
- Granny (10.10.10.15)
- Late (10.10.11.156)
- Paper (10.10.11.143)
- And many more...

### Tools

Useful scripts and references:
- `bigfile.sh`: Script for handling large files
- `docker_clean.txt`: Docker environment cleanup guide
- `pwntools-cheatsheet.md`: Quick reference for pwntools

## Setup & Usage

1. Clone the repository:
```bash
git clone https://github.com/ShundaZhang/htb.git
```

2. Most Python scripts require common security-related libraries:
- pwntools
- requests
- crypto
- web3 (for blockchain challenges)
- tensorflow/pytorch (for AI challenges)

3. For machine solutions:
- Most exploits are provided in Python/C/Powershell
- Some machines require specific tools that are included in their directories
- Check cmd.txt in each machine directory for step-by-step commands

## Challenge Categories Overview

### AI Challenges
- Focus on machine learning and data science problems
- Often require understanding of ML models and adversarial techniques
- Include both model training and exploitation

### Blockchain Challenges
- Smart contract vulnerabilities
- Web3 interaction
- Custom blockchain implementations
- Solidity exploits

### Crypto Challenges
- Classic cryptographic problems
- Modern cryptographic implementations
- Custom encryption schemes
- Protocol attacks

### Hardware Challenges
- Low-level programming
- Firmware analysis
- Protocol reverse engineering
- Signal processing

### Web Challenges
- Modern web vulnerabilities
- API security
- Client-side security
- Server-side vulnerabilities

## File Structure
- Each challenge has its own directory
- Solutions are typically in `dec.py` files
- Additional resources and files used in the challenge are included
- Machine directories contain relevant exploits and tools

## Notes
- Some solutions may require specific versions of tools or libraries
- All solutions are for educational purposes only
- Always follow HTB's rules and terms of service
- Do not use these exploits on unauthorized systems

## License

BSD 3-Clause License

Copyright (c) 2024, ShundaZhang
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

## Contributing
Feel free to open issues or submit pull requests for improvements or fixes. Please note that all contributions will be under the BSD 3-Clause license.

## Disclaimer
This repository is for educational purposes only. The authors are not responsible for any misuse of the information or code provided here.
