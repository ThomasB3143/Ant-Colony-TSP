# Ant colony optimisation solution to the travelling salesperson problem
Each .py file excluding node.py contains a diffent ACO algorithm implementing varying measures of optimisation for both efficiency and accuracy

Run the .py file to see the results!
- basic.py - Uses no additional optimisation, simply sends ant after ant, where pheremones added is directly proportional to length of total path
- decay.py - Uses an exponential decay factor to reduce pheremones added to already strong edges, ensures new, better edges are more likely to be discovered
