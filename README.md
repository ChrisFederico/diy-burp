# DIY Burp Mini-Suite (Educational Project)

**Warning:** This project is purely **educational**. Do not use it on third-party systems without authorization.

---

## Description

This project is a DIY mini-suite inspired by Burp Suite, developed exclusively for **educational purposes**. The goal is to understand how key web security tools work in practice, without relying on commercial software.

Currently, the only implemented module is:

- **Intruder (Sniper Attack)**: allows sending custom payloads to HTTP requests for targeted security testing on specific inputs.

The main objective is to **learn the HTTP request flow, manipulate parameters, and log responses**, without depending on full-featured external tools.

---

## Features

- Load raw HTTP requests from a configuration file.
- Send user-defined payloads on a single parameter (Sniper mode).
- Log results, including status code and response length.
- Easily extensible for adding other types of attacks in the future.

---

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/ChrisFederico/diy-burp.git
   cd diy-burp
    ```

1.  Prepare a request.txt file containing the raw HTTP request to test (check example file).
    
2.  Create a payloads.txt file with the payloads to send (one per line, check example file).
    
3. ```bash
   python path/to/intruder.py {request_file} {attack_type}
   ```
    

Results will be shown in the log with status code and response length for each payload.

Warnings
--------

*   **Educational purposes only**: do not test websites without permission.
    
*   Does not implement a proxy or HTTPS sniffing.
    
*   Extremely minimal compared to Burp Suite: intended only as a learning lab.
    

Future Extensions
-----------------

*   Other Intruder attack types (Pitchfork, Clusterbomb).
    
*   Basic proxy for intercepting and modifying requests in real time.
    
*   More detailed response reporting.
