#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - Check if a linked list has a cycle
 * @list: Pointer to the head of the linked list
 *
 * Return: 1 if there is a cycle, 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	fast = list;
	slow = list;

	while ((fast != NULL) && (fast->next != NULL))
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}
  
	return(0);
}
