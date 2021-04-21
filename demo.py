from captcha_solver.solver import Solver

pageurl = "https://www.rackroomshoes.com/"

proxy = "http://127.0.0.1"
auth_details = {"username": "proxy_username", "password": "proxy_password"}
args = ["--timeout 5"]
options = {"ignoreHTTPSErrors": True, "args": args}  
client = Solver(
    # With Proxy
    # pageurl, lang='en-US', options=options, proxy=proxy, proxy_auth=auth_details
    # Without Proxy
    pageurl, lang='en-US', options=options, retain_source=False
)

solution = client.loop.run_until_complete(client.start())
if solution:
    print(solution)
