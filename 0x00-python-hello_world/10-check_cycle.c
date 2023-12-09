#include "lists.h"

/**
 * check_cycle - checks if there is cycle
 * @list: the address of the first node
 *
 * Return: 0 if there is no cycle or 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *curr, *prev;

	curr = list->next;
	prev = list;
	if (list == NULL)
		return (0);
	while (curr != NULL)
	{
		if (curr->next == prev)
			return (1);
		curr = curr->next;
		prev = prev->next;
	}
	return (0);
}
