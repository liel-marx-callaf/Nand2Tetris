load,
output-file ShiftLR.out,
compare-to ShiftLR.cmp,
output-list RAM[5001]%D1.6.1 RAM[5002]%D1.6.1 RAM[5003]%D1.6.1 RAM[5004]%D1.6.1;

repeat 100000 {
  vmstep;
}

output;
