package two_sum_1

import (
	"reflect"
	"testing"
)

func Test_twoSum(t *testing.T) {
	type args struct {
		nums   []int
		target int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{name: "test case 1", args: args{nums: []int{2, 7, 11, 15}, target: 9}, want: []int{0, 1}},
		{name: "test case 2", args: args{nums: []int{3, 2, 4}, target: 6}, want: []int{1, 2}},
		{name: "test case 3", args: args{nums: []int{3, 3}, target: 6}, want: []int{0, 1}},
		{name: "test case 4", args: args{nums: []int{3, 2, 3}, target: 6}, want: []int{0, 2}},
		{name: "test case 5", args: args{nums: []int{3, 2, 4}, target: 5}, want: []int{0, 1}},
	}
	for _, tt := range tests {
		tt := tt
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()
			if got := twoSum(tt.args.nums, tt.args.target); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("twoSum() = %v, want %v", got, tt.want)
			}
		})
	}
}
