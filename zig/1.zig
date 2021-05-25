const std = @import("std");

pub fn main() !void {
    var ans: u32 = 0;
    var n: u16 = 3;
    while (n <= 1000) : (n += 1) {
        if (n % 3 == 0 or n % 5 == 0) ans += n;
    }
    std.debug.print("{}\n", .{ans});
}
