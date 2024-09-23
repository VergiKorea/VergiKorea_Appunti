module test;

logic [3:0] a,b,s;

initial begin
	$dumpfile("test.vcd");
	$dumpvars(0,test);

	# 17 a = 4'd10;
	b = 4'd2;
	# 10 b= 4'd5;
	# 10 b = 4'd0;
	# 10 $finish;
end


      adder dder_inst(a,b,s);

/*      initial
	      $monitor("At time %t, value = %h (%0d)",$time, value, value);
	   */
endmodule // test
