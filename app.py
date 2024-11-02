
from big_mind_mapping import bmm
from reverse_brainstorm import rb
from role_storming import rs
from scamper import sc
from six_hats import sh
from starburtsting import sb

user_query = "I am having a medical instagram page talking about chronique diseases and how to deal with them. I need ideas for posts that can help me grow my page and reach more people."

# testing bmm
# save the text from the bmm function into a text file 
# with open("bmm_output.txt", "w") as f:
#     f.write(bmm(user_query))
# with open("rb_output.txt", "w") as f:
#     f.write(rb(user_query))

# with open("rs_output.txt", "w") as f:
#     f.write(rs(user_query))

with open("sc.txt", "w") as f:
    f.write(sc(user_query))

# with open("sh.txt", "w") as f:
#     f.write(sh(user_query))

# with open("sb.txt", "w") as f:
#     f.write(sb(user_query))
