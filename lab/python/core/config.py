zap_url = "http://localhost:9999"

max_duration = 1 # Number of minutes to spider and active-scan for (default 1)

# target_auth can be ignored if we're not using 'scanAsUser()' (for spider or ascan)
target_auth = {
	"login_url": "https://www.example.com/profile/signin.html",
	"user": "foo@example.com",
	"pw": "bar"
}