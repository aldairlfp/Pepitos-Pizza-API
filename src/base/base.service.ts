import { Injectable } from '@nestjs/common';
import { CreateBaseDto } from './dto/create-base.dto';
import { UpdateBaseDto } from './dto/update-base.dto';
import { Base } from './entities/base.entity';
import { BaseRepository } from './repositories/base.repository';

@Injectable()
export class BaseService {
  constructor(private baseRepository: BaseRepository) {}

  private bases: Base[] = [
    { id: 1, name: 'Base grande', price: 120, available: true },
  ];

  async create(createBaseDto: CreateBaseDto): Promise<Base> {
    const newBase = { ...createBaseDto };

    const base = new Base();
    base.name = newBase.name;
    base.price = newBase.price;
    base.available = newBase.available;

    const savedBase = await this.baseRepository.create(base);

    return savedBase;
  }

  async findAll(): Promise<Base[]> {
    return await this.baseRepository.findAll();
  }

  async findOne(id: number): Promise<Base> {
    return await this.baseRepository.findOne(id);
  }

  update(id: number, updateBaseDto: UpdateBaseDto): Base {
    return this.bases[0];
  }

  remove(id: number): Base {
    return this.bases[0];
  }
}
