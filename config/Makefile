
HOSTNAME := `hostname -s`

leetcode.toml: leetcode-rust.toml leetcode-go.toml leetcode-python.toml
	cp leetcode-python.toml leetcode.toml

leetcode-python.toml: templates/leetcode-front.toml templates/python_insert.tpl $(HOSTNAME)-leetcode-creds.toml templates/leetcode-back.toml
	cat templates/leetcode-front.toml templates/python_insert.tpl $(HOSTNAME)-leetcode-creds.toml templates/leetcode-back.toml > leetcode-python.toml

.PHONY: clean

clean:
	rm -f leetcode-python.toml
	rm -f leetcode-go.toml
	rm -f leetcode-rust.toml
	rm -f leetcode.toml
	rm -f *-leetcode-creds.toml

leetcode-rust.toml: templates/leetcode-front.toml templates/rust_insert.tpl $(HOSTNAME)-leetcode-creds.toml templates/leetcode-back.toml
	cat templates/leetcode-front.toml templates/rust_insert.tpl $(HOSTNAME)-leetcode-creds.toml templates/leetcode-back.toml > leetcode-rust.toml

leetcode-go.toml: templates/leetcode-front.toml templates/go_insert.tpl $(HOSTNAME)-leetcode-creds.toml templates/leetcode-back.toml
	cat templates/leetcode-front.toml templates/go_insert.tpl $(HOSTNAME)-leetcode-creds.toml templates/leetcode-back.toml > leetcode-go.toml

