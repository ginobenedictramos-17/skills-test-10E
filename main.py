from pyscript import display, document
#some parts of pyscript modified by copilot tool to debug
#internal css in index.html was made better through copilot suggestions
def ordering_form(e):
    item1 = document.getElementById("taco1")
    item2 = document.getElementById("taco2")
    item3 = document.getElementById("taco3")
    address = document.getElementById("address").value
    name = document.getElementById("name").value
    number = document.getElementById("number").value
    mode = document.getElementById("payment").value

    total = (float(item1.value) * item1.checked +
             float(item2.value) * item2.checked +   
            float(item3.value) * item3.checked)

    display(f"The total amount is Php{total}. We will contact {name} at {number} when the order has arrived at {address}, to be paid through {mode}", target='div2')
