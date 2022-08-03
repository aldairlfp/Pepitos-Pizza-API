import { Test, TestingModule } from '@nestjs/testing';
import { AddedController } from './added.controller';
import { AddedService } from './added.service';

describe('AddedController', () => {
  let controller: AddedController;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      controllers: [AddedController],
      providers: [AddedService],
    }).compile();

    controller = module.get<AddedController>(AddedController);
  });

  it('should be defined', () => {
    expect(controller).toBeDefined();
  });
});
