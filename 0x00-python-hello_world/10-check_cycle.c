#include "lists.h"

/**
 * check_cycle - checks if the linked list have a cycle
 * @list: address of the node
 *
 * Return: 1 if there is cycle otherwise 0
 */
int check_cycle(listint_t *list)
{
	if (list == NULL || list->next == NULL)
		return (0);
	listint_t *current, *temp;
	current = list;
	temp = current->next;
	while ((current != NULL) && (current->next != NULL) && (temp->next != NULL) )
	{
		if (current == temp)
			return (1);
		current = current->next;
		temp = temp->next;
	}
	return (0);
}
