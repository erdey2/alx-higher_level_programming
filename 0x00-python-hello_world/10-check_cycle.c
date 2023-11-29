#include "lists.h"

/**
 * check_cycle - checks if the linked list have a cycle
 * @list: address of the node
 *
 * Return: 1 if there is cycle otherwise 0
 */
int check_cycle(listint_t *list)
{
	while (list)
	{
		list = list->next;
		if (list->next == NULL)
			return (0);
	}
	return (1);
}
