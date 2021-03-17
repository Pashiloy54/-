begin
  var first, two: real; 
  var answer: string;
  write('Введите первое число: '); readln(first);
  write('Введите второе число: '); readln(two);
  write('Знак: '); readln(answer);
  if answer = '+' then
    write(first + two);
  if answer = '-' then
    write(first - two);
  if answer = '*' then
    write(first * two);
  if answer = '/' then
    write(first / two)
  else
    write('НЕВЕРНЫЙ ЗНАК!!!')
end.