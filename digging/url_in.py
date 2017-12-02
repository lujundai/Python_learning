import re

string = "X2 Handover (eNB 42 -> eNB 1) completed "
pattern = re.compile("X2\s+Handover\s+\(eNB\s+(\d+)\s+->\s+eNB\s+1\)\s+completed")
#string = "X2 Handover (eNB 1 -> eNB 42) completed "
#pattern = re.compile("X2\s+Handover\s+\(eNB\s+1\s+->\s+eNB\s+(\d+)\)\s+completed")
match = re.match(pattern,string)
if match:
	print match.group()
else:
	print "cannot find strings"