from stack import Stack


'''

    Build browser navigation — Medium
    Create a BrowserHistory class using two stacks. Start on "Home" and implement visit(page), back(), forward() and current().
    Visiting a new page must clear the forward history. If there is nowhere to go back or forward, keep the current page unchanged.
    Check this sequence:
    Action	Current page
    Visit "Python"	"Python"
    Visit "Stacks"	"Stacks"
    Back	"Python"
    Forward	"Stacks"
    Back, then visit "Queues"	"Queues"
    Forward	"Queues"

'''