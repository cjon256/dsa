
HOSTNAME := `hostname -s`
CREDS_FILE := $(HOSTNAME)-leetcode-creds.toml

leetcode.toml: leetcode-rust.toml leetcode-go.toml leetcode-python.toml
	cp leetcode-python.toml leetcode.toml

.PHONY: $(CREDS_FILE)

$(CREDS_FILE):
	@if [ ! -f $(CREDS_FILE) ]; then echo "Please login to Leetcode on Firefox and run capture-cookies to create $(CREDS_FILE) file."; exit 1; fi

.PHONY: clean

clean:
	rm -f leetcode-python.toml
	rm -f leetcode-go.toml
	rm -f leetcode-rust.toml
	rm -f leetcode.toml
	rm -f *-leetcode-creds.toml

leetcode-python.toml: templates/leetcode-front.toml templates/python_insert.tpl $(CREDS_FILE) templates/leetcode-back.toml
	cat templates/leetcode-front.toml templates/python_insert.tpl $(HOSTNAME)-leetcode-creds.toml templates/leetcode-back.toml > leetcode-python.toml

leetcode-rust.toml: templates/leetcode-front.toml templates/rust_insert.tpl $(CREDS_FILE) templates/leetcode-back.toml
	cat templates/leetcode-front.toml templates/rust_insert.tpl $(CREDS_FILE) templates/leetcode-back.toml > leetcode-rust.toml

leetcode-go.toml: templates/leetcode-front.toml templates/go_insert.tpl $(CREDS_FILE) templates/leetcode-back.toml
	cat templates/leetcode-front.toml templates/go_insert.tpl $(CREDS_FILE) templates/leetcode-back.toml > leetcode-go.toml

