#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @head: - Head of the linked list
 * Return: 0 if no cycle and 1 if there is a cycle
 */
int check_cycle(listint_t *head)
{
	listint_t *first, *last;

	first = head;
	last = head;
	while (last != NULL)
	{
		if (last->next == NULL)
			return (0);
		if (last->next == first)
			return (1);
		last = last->next;
	}
	return (0);
}
