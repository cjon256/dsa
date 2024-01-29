
leetcode.toml: leetcode-rust.toml leetcode-go.toml leetcode-python.toml
	cp leetcode-python.toml leetcode.toml

leetcode-python.toml: templates/leetcode-front.toml templates/python_insert.tpl templates/leetcode-back.toml
	cat templates/leetcode-front.toml templates/python_insert.tpl templates/leetcode-back.toml > leetcode-python.toml.in
	op run --no-masking --env-file=/Users/cjon/src/leetcode/config/leetcodecreds.env envsubst < /Users/cjon/src/leetcode/config/leetcode-python.toml.in > /Users/cjon/src/leetcode/config/leetcode-python.toml
	rm -f leetcode-python.toml.in

.PHONY: clean

clean:
	rm -f leetcode-python.toml
	rm -f leetcode-go.toml
	rm -f leetcode-rust.toml
	rm -f leetcode.toml

leetcode-rust.toml: templates/leetcode-front.toml templates/rust_insert.tpl templates/leetcode-back.toml
	cat templates/leetcode-front.toml templates/rust_insert.tpl templates/leetcode-back.toml > leetcode-rust.toml.in
	op run --no-masking --env-file=/Users/cjon/src/leetcode/config/leetcodecreds.env envsubst < /Users/cjon/src/leetcode/config/leetcode-rust.toml.in > /Users/cjon/src/leetcode/config/leetcode-rust.toml
	rm -f leetcode-rust.toml.in

leetcode-go.toml: templates/leetcode-front.toml templates/go_insert.tpl templates/leetcode-back.toml
	cat templates/leetcode-front.toml templates/go_insert.tpl templates/leetcode-back.toml > leetcode-go.toml.in
	op run --no-masking --env-file=/Users/cjon/src/leetcode/config/leetcodecreds.env envsubst < /Users/cjon/src/leetcode/config/leetcode-go.toml.in > /Users/cjon/src/leetcode/config/leetcode-go.toml
	rm -f leetcode-go.toml.in

