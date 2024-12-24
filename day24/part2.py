# vals = {}

# lines = list(open(0))

# print("digraph {")

# for line in lines:
#     if ": " in line:
#         name, val = line.strip().split(": ")
#         print(f"{name};")
#     else:
#         parts = line.split()
#         if not parts: continue
#         lhs = parts[0]
#         rhs = parts[2]
#         dst = parts[4]
#         print(f"{parts[4]} [label=\"{parts[4]} = {parts[1]}\"];")
#         print(f"{parts[0]} -> {parts[4]};")
#         print(f"{parts[2]} -> {parts[4]};")

# print("}")

# Pipe the above into `dot -Tpng -o graph.png` and look for swaps manually.
# The structure is extremely simple so it's not too hard but a bit time
# consuming.

# Found manually:
#  z13-vcv
#  z19-vwp
#  mps-z25
#  cqm-vjv

print(",".join(sorted(["z13","vcv","z19","vwp","mps","z25","cqm","vjv"])))
