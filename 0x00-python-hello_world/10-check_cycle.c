#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *prev = list, *ahead = list;

	if (!list)
		return (0);

	while (ahead->next && ahead->next->next)
	{
		prev = prev->next;
		ahead = ahead->next->next;
		if (ahead == prev)
			return (1);
	}
	return (0);
}
