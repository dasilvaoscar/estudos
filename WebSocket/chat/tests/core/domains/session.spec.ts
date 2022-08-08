import { Session } from '@/core/domains/session';
import { randomUUID } from 'crypto';

test('Create session', () => {
  const UUID = randomUUID();
  const firstUserUUID = randomUUID();
  const secondUserUUID = randomUUID();

  const users = [firstUserUUID, secondUserUUID];

  const sessionInfo = {
    id: UUID,
    usersUUID: users,
  };

  const session = new Session(sessionInfo);

  expect(session.id).toEqual(UUID);
  console.log(`Session created: ${session.id}`);

  expect(session.usersUUID).toEqual(users);
  console.log(`Users: ${JSON.stringify(session.usersUUID)}`);
});
