#include "lists.h"

/**
 * check_cycle - checks if the linked list have a cycle
 * @list: address of the node
 *
 * Return: 1 if there is cycle otherwise 0
 */
int check_cycle(listint_t *list)
{
	list_t *temp;

	temp = list;
	while (temp)
	{
		temp = temp -> next;
		if (temp == NULL)
			return (0)
	}
	return (1);

}
