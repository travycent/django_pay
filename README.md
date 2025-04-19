# Django Pay

Django Pay is a simple payment platform designed to work seamlessly with Flutterwave, DPO, and most other payment platforms. The solution is aimed at vending internet packages using a self service wifi platform which includes a voucher, connection to a microtic router and autologin.This is an open-source project aimed at helping anyone who wants to start building a payment system for selling hotspot internet with Django.

## Requirements
- Python3.10
- Python Virtualenv
- Weasy Print [Docs](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html)

## How to run
Create a virtualenv if you do not have one.
```
python -m venv venv
```
Ensure you are creating a virtual env using python3.

Activate the virtualenv using the command
```
source venv/bin/activate
```
If you are using vscode, opening the terminal will automatically activate the virtualenv.

Create a file called `.env`. This is where we will put the environment variables.
Use `.env_example` to populate your `.env` file.