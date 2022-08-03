import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHello(): object {
    const message = 'Hello World!';
    const user = {
      name: 'Aldair',
      age: 23,
    };
    console.log(user);
    return user;
  }
}
