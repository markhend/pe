const std = @import("std");

pub fn main() !void {
    var n: u64 = 600851475143;
    var f: u64 = 2;
    while (n > 1) {
        if (n % f == 0) n /= f else f += 1;
    }
    std.debug.print("{}\n", .{f});
}
