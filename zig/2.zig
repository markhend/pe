const std = @import("std");

pub fn main() !void {
    var prev: u32 = 1;
    var curr: u32 = 2;
    var ans: u32 = 0;
    var next: u32 = undefined;

    while (curr < 4000000) {
        if (curr % 2 == 0) ans += curr;
        next = prev + curr;
        prev = curr;
        curr = next;
    }

    std.debug.print("{}\n", .{ans});
}
