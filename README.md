# Solo (?) Pre-Dev/Mocking Environment

At the moment, files here are intended to be experimental and not representative of future development.

For information, links, and documentation regarding the UI-Template [Volt React Dashboard Bootstrap 5](https://demo.themesberg.com/volt-react-dashboard), please see "TEMPLATE_README.md" in this repo.

## Initial Installation and Setup

1. Make sure you have [Node.js](https://nodejs.org/en/) installed.
1. Clone into this repository with `git clone https://github.com/lagunaelectric/ui-test`
1. In the project root ("/ui-test"), run `npm install` to install project dependencies.


## Spinning up the project

1. Start the Flask backend like so:
    1. cd into ui-test/api with `cd api`
    1. Activate the virtual env with `venv/Scripts/activate.ps1`(powershell)
        - You may need to use ...`activate.bat`(cmd) or something else depending on shell/OS
    1. Start the server with `flask run --no-debugger`
1. Return to the root directory (you will likely need to open another shell instance)
1. Run `npm start`


## Current testing page for api integration

1. Navigate to https://localhost:3000/#/apitest
1. Clicking the button "Send Request" SHOULD initiate the following:
    1. Send a request to the Flask api route "/test_message"
    1. Receive a response with object { message: "hello world" }
    1. Update the area below "Response message" with that message (hello world)  