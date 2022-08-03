import { Injectable } from '@nestjs/common';
import { CreateClientDto } from './dto/create-client.dto';
import { UpdateClientDto } from './dto/update-client.dto';

@Injectable()
export class ClientService {
  private users: any = [
    {
      id: 1,
      name: 'Aldair',
    },
    {
      id: 2,
      name: 'Glenda',
    },
    {
      id: 3,
      name: 'Yero',
    },
  ];

  create(createClientDto: CreateClientDto) {
    return 'This action adds a new client';
  }

  findAll() {
    return this.users;
    return `This action returns all client`;
  }

  findOne(id: number) {
    return this.users.find((user) => user.id === id);
  }

  update(id: number, updateClientDto: UpdateClientDto) {
    return `This action updates a #${id} client`;
  }

  remove(id: number) {
    return `This action removes a #${id} client`;
  }
}
