class   Node:
    def __init__(self,coeff,expo):
        self.coeff=coeff
        self.expo=expo
        self.next=None
def create_polynomial():
        head=None
        n=int(input("Enter the terms:"))
        for i in range(n):
            co=int(input("Enter the coefficient:"))
            ex=int(input("Enter the exponent:"))
            newnode=Node(co,ex)
            if head is None or ex>head.expo:
                newnode.next=head
                head=newnode
            else:
                temp=head
                while temp.next is not None and temp.next.expo>=ex:
                    temp=temp.next
                newnode.next=temp.next
                temp.next=newnode
        return head

def add_polynomial(poly1,poly2):
    result_head=None
    while poly1 and poly2:
        if poly1.expo>poly2.expo:
            result_head=insert_term(result_head,poly1.coeff,poly1.expo)
            poly1=poly1.next
        elif poly1.expo<poly2.expo:
            result_head=insert_term(result_head,poly2.coeff,poly2.expo)
            poly2=poly2.next
        else:
            sum_coeff=poly1.coeff+poly2.coeff
            if sum_coeff:
                  result_head=insert_term(result_head,sum_coeff,poly1.expo)
             poly1=poly1.next
             poly2=poly2.next
    while poly1:
        result_head=insert_term(result_head,poly1.coeff,poly1.expo)
        poly1=poly1.next
    while poly2:
        result_head=insert_term(result_head,poly2.coeff,poly2.expo)
        poly2=poly2.next
    return result_head
def insert_term(head,coeff,expo):
    newnode= Node(coeff,expo)
    if not head or expo>head.expo:
        nwenode.next=head
        head=newnode
    else:
        temp=head
        while temp.next and temp.next.expo>=expo:
            temp=temp.next
        newnode.next=temp.next
        temp.next=newnode
 def display_polynomial(head):
        if head is None:
            print("No polynomial")
        else:
            temp=head
            while temp is not None:
                print(f"({temp.coeff}x^{temp.expo})",end="")
                temp=temp.next
                if temp is not None:
                    print("+",end="")
                else:
                    print(  
             
                       


















def display_polynomial(head):
        if head is None:
            print("No polynomial")
        else:
            temp=head
            while temp is not None:
                print(f"({temp.coeff}x^{temp.expo})",end="")
                temp=temp.next
                if temp is not None:
                    print("+",end="")
                else:
                    print()
