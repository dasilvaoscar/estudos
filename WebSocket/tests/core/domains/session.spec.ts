import { Session } from '../../../src/core/domains/session';
import { randomUUID } from 'crypto';

test('Create session', () => {
  const UUID = randomUUID();
  const firstUserUUID = randomUUID();
  const secondUserUUID = randomUUID();

  const session = new Session({
    id: UUID,
    usersUUID: [firstUserUUID, secondUserUUID],
  });

  expect(session.id).toBe(UUID);
  expect(session.usersUUID).toEqual([firstUserUUID, secondUserUUID]);
});
