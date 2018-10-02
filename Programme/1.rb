#PennyBoki @ </dream.in.code>
puts 'Enter a number'
STDOUT.flush
string1 = gets.chomp
x = string1.to_i
puts 'The Fibonacci Series'
fib1 = 1
fib2 = 1
runner = 0
puts fib1.to_s
puts fib2.to_s
while runner<x
runner += 1
fib3 = fib1 + fib2;
fib1 = fib2;
fib2 = fib3; 
puts fib3.to_s
end
