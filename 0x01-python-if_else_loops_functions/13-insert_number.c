#include "lists.h"

/**
 * insert_node - insert a node into a sorted linked list
 * @head: the address of the first node
 * @number: the data to be inserted
 *
 * Return: the address of the newly inserted element
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *prev = NULL, *temp;

	curr = *head;
	while (curr && number >= curr->n)
	{
		prev = curr;
		curr = curr->next;
	}
	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return (NULL);
	temp->n = number;
	if (number < (*head)->n)
	{
		temp->next = *head;
		*head = temp;
	}
	if (curr->next == NULL)
	{
		curr->next = temp;
		temp->next = NULL;
	}
	else
	{
		temp->next = curr;
		prev->next = temp;
	}
	return (temp);
}
