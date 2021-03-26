from captcha_solver.solver import Solver

pageurl = "https://www.rackroomshoes.com/"

proxy = "127.0.0.1:1000"
auth_details = {"username": "user", "password": "pass"}
args = ["--timeout 5"]
options = {"ignoreHTTPSErrors": True, "args": args}  # References: https://miyakogi.github.io/pyppeteer/reference.html
client = Solver(
    # With Proxy
    # pageurl, lang='en-US', options=options, proxy=proxy, proxy_auth=auth_details
    # Without Proxy
    pageurl, lang='en-US', options=options
)

solution = client.loop.run_until_complete(client.start())
if solution:
    print(solution)
