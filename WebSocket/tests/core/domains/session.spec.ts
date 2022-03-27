import { Session } from '@/core/domains/session';
import { Message } from '@/core/domains/message';
import { WinstonLogger } from '@/infra/loggers/winston';
import { randomUUID } from 'crypto';

const logger = new WinstonLogger('Tests Session');

test('Create session', () => {
  const UUID = randomUUID();
  const firstUserUUID = randomUUID();
  const secondUserUUID = randomUUID();

  const users = [firstUserUUID, secondUserUUID];

  const messages = [
    new Message({ userUUID: firstUserUUID, message: 'Oi' }),
    new Message({ userUUID: secondUserUUID, message: 'Oila kkkk' }),
  ];

  const sessionInfo = {
    id: UUID,
    usersUUID: users,
    messages: messages,
  };

  const session = new Session(sessionInfo);

  expect(session.id).toEqual(UUID);
  logger.log(`Session created: ${session.id}`);

  expect(session.usersUUID).toEqual(users);
  logger.log(`Users: ${JSON.stringify(session.usersUUID)}`);

  expect(session.messages).toEqual(messages);
  logger.log(`Messages: ${JSON.stringify(session.messages)}`);
});
