import { Module } from '@nestjs/common';
import { BaseService } from './base.service';
import { BaseController } from './base.controller';
import { BaseRepository } from './repositories/base.repository';

@Module({
  controllers: [BaseController],
  providers: [BaseService, BaseRepository],
})
export class BaseModule {}
