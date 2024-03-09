# pip install proxy-checking
from proxy_checking import ProxyChecker

checker = ProxyChecker()
r = checker.check_proxy('<ip>:<port>')
print(r)
