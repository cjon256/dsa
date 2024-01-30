//  Category: algorithms
//  Level: Easy
//  Percent: 53.10369%

//  Given two binary strings a and b, return their sum as a binary string.
//
//
//  Example 1:
//  Input: a = "11", b = "1"
//  Output: "100"
//  Example 2:
//  Input: a = "1010", b = "1011"
//  Output: "10101"
//
//
//  Constraints:
//
//
//  	1 <= a.length, b.length <= 10⁴
//  	a and b consist only of '0' or '1' characters.
//  	Each string does not contain leading zeros except for the zero itself.
//

//  start_marker
impl Solution {
    pub fn add_binary(a: String, b: String) -> String {
        // create vectors of u126s from the strings
        let mut a = a
            .chars()
            .map(|c| c.to_digit(10).unwrap() as u128)
            .collect::<Vec<u128>>();
        let mut b = b
            .chars()
            .map(|c| c.to_digit(10).unwrap() as u128)
            .collect::<Vec<u128>>();

        // pad the shorter vector with zeros
        if a.len() > b.len() {
            b.reverse();
            b.resize(a.len(), 0);
            b.reverse();
        } else {
            a.reverse();
            a.resize(b.len(), 0);
            a.reverse();
        }

        // add a leading zero to each vector to account for carry
        a.insert(0, 0);
        b.insert(0, 0);

        // processing the arrays in reverse order, add each element of a and b along with carry from previous add
        let mut carry = 0;
        let mut sum: Vec<u128> = Vec::new();
        for i in (0..a.len()).rev() {
            let mut s = a[i] + b[i] + carry;
            if s > 1 {
                carry = 1;
                s -= 2;
            } else {
                carry = 0;
            }
            sum.insert(0, s);
        }

        // convert the resulting sum back into a string
        let result = sum
            .iter()
            .map(|&x| x.to_string())
            .collect::<Vec<String>>()
            .join("");
        // trim leading zeros
        let retval = result.trim_start_matches('0').to_string();
        if retval == "".to_string() {
            "0".to_string()
        } else {
            retval
        }
    }
}
//  end_marker
// impl Solution_prime {
//     pub fn add_binary_ganky(a: String, b: String) -> String {
//         let ca = a.chars().rev().collect::<Vec<char>>();
//         let cb = b.chars().rev().collect::<Vec<char>>();
//         let mut carry = 0;
//         let len_a = ca.len();
//         let len_b = cb.len();
//         let larger = if len_a > len_b { &ca } else { &cb };
//         let smaller = if len_a > len_b { &cb } else { &ca };
//         let length_differece = larger.len() - smaller.len();
//         let mut result = String::new();
//         for idx in 0..larger.len() {
//             let mut sum = carry;
//             if idx < smaller.len() {
//                 sum += smaller[idx].to_digit(10).unwrap();
//             }
//             sum += larger[idx].to_digit(10).unwrap();
//             carry = sum / 2;
//             result.push_str(&(sum % 2).to_string());
//         }
//         result.push_str(&(carry % 2).to_string());
//         if result.trim_start_matches('0') == "" {
//             "0".to_string()
//         } else {
//             result
//                 .chars()
//                 .rev()
//                 .collect::<String>()
//                 .trim_start_matches('0')
//                 .to_string()
//         }
//     }
//     pub fn bad_add_binary(a: String, b: String) -> String {
//         let int_a = i128::from_str_radix(&a, 2);
//         let int_b = i128::from_str_radix(&b, 2);
//         match (int_a, int_b) {
//             (Ok(a), Ok(b)) => format!("{:b}", a + b),
//             _ => "0".to_string(),
//         }
//     }
// }

pub struct Solution;

#[cfg(test)]
mod tests {
    use super::*;

    use rstest::rstest;

    #[rstest]
    #[case("11", "1", "100")]
    #[case("1010", "1011", "10101")]
    #[case("0", "0", "0")]
    #[case("0", "1", "1")]
    #[case("1", "0", "1")]
    #[case("1", "1", "10")]
    #[case("111", "111", "1110")]
    #[case("111", "1111", "10110")]
    #[case("1111", "1111", "11110")]
    #[case("11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "1",
          "100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")]
    fn case(#[case] a: String, #[case] b: String, #[case] expected: String) {
        let actual = Solution::add_binary(a, b);
        assert_eq!(actual, expected);
    }
}
