import { Base } from '../entities/base.entity';
import { AppDataSource } from '../../main';

export class BaseRepository {
  baseRepository = AppDataSource.manager.getRepository(Base);

  async findAll(): Promise<Base[]> {
    return await this.baseRepository.find();
  }

  async findOne(id: number): Promise<Base> {
    return this.baseRepository.findOneBy({ id: id });
  }

  async create(base: Base): Promise<Base> {
    await AppDataSource.manager.save(base);
    return base;
  }
}
