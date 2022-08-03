import { Module } from '@nestjs/common';
import { AddedService } from './added.service';
import { AddedController } from './added.controller';

@Module({
  controllers: [AddedController],
  providers: [AddedService],
})
export class AddedModule {}
