#include "lists.h"
#include <stdlib.h>

/**
*insert_node - a function in that inserts
*a number into a sorted singly linked list
*
*@head: a pointer to the head
*@number: number to be inserted
*
*Return: the address of the new node, or NULL
*/

listint_t *insert_node(listint_t **head, int number)
{
listint_t *newnode, *temp;
newnode = malloc(sizeof(listint_t));
newnode->n = number;
if (newnode == NULL)
{
return (NULL);
}
if ((*head) == NULL || number < (*head)->n)
{
newnode->next = (*head);
(*head) = newnode;
return (newnode);
}
else
{
temp = (*head);
while (temp->next != NULL && number > temp->next->n)
{
temp = temp->next;
}
newnode->next = temp->next;
temp->next = newnode;
}
return (newnode);
}
